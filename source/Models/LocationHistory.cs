namespace StudentTracker.Models
{
    public class LocationHistory
    {
        public int HistoryID { get; set; }
        public int StudentID { get; set; }
        public List<Location> Locations { get; set; }
        public DateTime Date { get; set; }
    }
}
