"""
Admin Commands - Secure database management
Requires admin user ID authentication
"""

import os
import logging
from sqlalchemy import text
from models import engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get admin user ID from environment
ADMIN_USER_IDS = os.getenv("ADMIN_USER_IDS", "").split(",")
ADMIN_USER_IDS = [uid.strip() for uid in ADMIN_USER_IDS if uid.strip()]

def is_admin(user_id):
    """Check if user is authorized admin"""
    return str(user_id) in ADMIN_USER_IDS

def reset_database(user_id, confirmation_code=None):
    """
    Reset database - DESTRUCTIVE OPERATION
    Requires admin user ID and confirmation code
    """
    # Verify admin status
    if not is_admin(user_id):
        logger.warning(f"Unauthorized database reset attempt by user {user_id}")
        return {
            "success": False,
            "message": "❌ Unauthorized: You are not an admin",
            "error": "UNAUTHORIZED"
        }
    
    # Require confirmation code
    expected_code = "RESET_ALL_DATA"
    if confirmation_code != expected_code:
        return {
            "success": False,
            "message": f"⚠️ Confirmation required. Send: /reset {expected_code}",
            "error": "CONFIRMATION_REQUIRED"
        }
    
    try:
        with engine.connect() as conn:
            # Get stats before deletion
            stats_query = text("SELECT COUNT(*) as count, COALESCE(SUM(profit), 0) as total_profit FROM trade_logs")
            stats = conn.execute(stats_query).fetchone()
            trade_count = stats[0]
            total_profit = stats[1]
            
            # Delete all trades
            delete_query = text("DELETE FROM trade_logs")
            conn.execute(delete_query)
            conn.commit()
            
            logger.info(f"✅ Database reset by admin {user_id}")
            logger.info(f"   Deleted {trade_count} trades worth ${total_profit:,.2f}")
            
            return {
                "success": True,
                "message": f"✅ Database reset successful!\n\n📊 Deleted:\n- {trade_count} trades\n- ${total_profit:,.2f} total profit\n\nDatabase is now empty.",
                "trades_deleted": trade_count,
                "profit_deleted": float(total_profit)
            }
            
    except Exception as e:
        logger.error(f"Database reset failed: {e}")
        return {
            "success": False,
            "message": f"❌ Database reset failed: {str(e)}",
            "error": str(e)
        }

def get_database_stats(user_id):
    """Get current database statistics"""
    if not is_admin(user_id):
        return {
            "success": False,
            "message": "❌ Unauthorized: You are not an admin"
        }
    
    try:
        with engine.connect() as conn:
            stats_query = text("""
                SELECT 
                    COUNT(*) as total_trades,
                    COUNT(CASE WHEN profit > 0 THEN 1 END) as winning_trades,
                    COUNT(CASE WHEN profit < 0 THEN 1 END) as losing_trades,
                    COALESCE(SUM(profit), 0) as total_profit,
                    COALESCE(AVG(profit), 0) as avg_profit,
                    COALESCE(MAX(profit), 0) as max_profit,
                    COALESCE(MIN(profit), 0) as max_loss
                FROM trade_logs
            """)
            stats = conn.execute(stats_query).fetchone()
            
            total = stats[0]
            wins = stats[1]
            losses = stats[2]
            win_rate = (wins / total * 100) if total > 0 else 0
            
            message = f"""📊 DATABASE STATISTICS

📈 Trades: {total:,}
✅ Wins: {wins} ({win_rate:.1f}%)
❌ Losses: {losses}

💰 Total Profit: ${stats[3]:,.2f}
📊 Avg Profit: ${stats[4]:,.2f}
🚀 Best Trade: ${stats[5]:,.2f}
📉 Worst Trade: ${stats[6]:,.2f}
"""
            
            return {
                "success": True,
                "message": message,
                "stats": {
                    "total_trades": total,
                    "winning_trades": wins,
                    "losing_trades": losses,
                    "win_rate": win_rate,
                    "total_profit": float(stats[3]),
                    "avg_profit": float(stats[4]),
                    "max_profit": float(stats[5]),
                    "max_loss": float(stats[6])
                }
            }
    except Exception as e:
        logger.error(f"Failed to get stats: {e}")
        return {
            "success": False,
            "message": f"❌ Failed to get stats: {str(e)}"
        }

def delete_specific_trade(user_id, txid):
    """Delete a specific trade by TXID"""
    if not is_admin(user_id):
        return {
            "success": False,
            "message": "❌ Unauthorized: You are not an admin"
        }
    
    try:
        with engine.connect() as conn:
            delete_query = text("DELETE FROM trade_logs WHERE txid = :txid")
            result = conn.execute(delete_query, {"txid": txid})
            conn.commit()
            
            if result.rowcount > 0:
                logger.info(f"Admin {user_id} deleted trade {txid}")
                return {
                    "success": True,
                    "message": f"✅ Trade {txid} deleted successfully"
                }
            else:
                return {
                    "success": False,
                    "message": f"❌ Trade {txid} not found"
                }
    except Exception as e:
        logger.error(f"Failed to delete trade: {e}")
        return {
            "success": False,
            "message": f"❌ Failed to delete trade: {str(e)}"
        }

# Command handler for bot integration
def handle_admin_command(user_id, command, args):
    """Handle admin commands from Telegram bot"""
    command = command.lower()
    
    if command == "/reset":
        confirmation = args[0] if args else None
        return reset_database(user_id, confirmation)
    
    elif command == "/stats":
        return get_database_stats(user_id)
    
    elif command == "/delete":
        if not args:
            return {
                "success": False,
                "message": "❌ Usage: /delete <TXID>"
            }
        txid = args[0]
        return delete_specific_trade(user_id, txid)
    
    elif command == "/help" or command == "/admin":
        return {
            "success": True,
            "message": """🔐 ADMIN COMMANDS

📊 /stats - Get database statistics
🗑️ /delete <TXID> - Delete specific trade
⚠️ /reset RESET_ALL_DATA - Reset entire database

⚠️ All commands require admin authorization
"""
        }
    
    else:
        return {
            "success": False,
            "message": f"❌ Unknown command: {command}\nType /admin for help"
        }

__all__ = ['handle_admin_command', 'is_admin', 'reset_database', 'get_database_stats']

if __name__ == "__main__":
    print("Admin Commands Module")
    print(f"Configured admin IDs: {len(ADMIN_USER_IDS)}")
    if not ADMIN_USER_IDS:
        print("⚠️  No admin IDs configured. Set ADMIN_USER_IDS environment variable.")
