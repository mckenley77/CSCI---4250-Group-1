namespace StudentTracker.Models
{
    public class LocationHistory
    {
        public int HistoryID { get; set; }
        public int StudentID { get; set; }
        //no date because date is held in locations
        public List<Location> Locations { get; set; }
    }
}
