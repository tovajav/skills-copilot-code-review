"""
Announcements router for Mergington High School API
"""

from fastapi import APIRouter
import logging
from ..database import announcements_collection

# Set up logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["announcements"])


@router.get("/announcement")
async def get_announcement():
    """Get the current active announcement"""
    try:
        announcement = announcements_collection.find_one({"_id": "current"})
        
        if not announcement:
            return {"message": "", "active": False}
        
        return {
            "message": announcement.get("message", ""),
            "active": announcement.get("active", False)
        }
    except Exception as e:
        # Log error but don't expose to frontend
        logger.error(f"Error retrieving announcement: {e}")
        return {"message": "", "active": False}
