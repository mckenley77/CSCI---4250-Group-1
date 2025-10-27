namespace StudentTracker.Models
{
    public class Location
    {
        public int LocationID { get; set; }
        public int UserID { get; set; }
        public double Latitute { get; set; }
        public double Longitute { get; set; }

        public string Address { get; set; }
        public DateTime Timestamp { get; set; }
        public float Accuracy { get; set; }
    }
}
