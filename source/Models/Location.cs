using System.Text.Json.Serialization;

namespace StudentTracker.Models
{
    public class Location
    {
        [JsonPropertyName("id")]
        public int LocationID { get; set; } = 0;

        [JsonPropertyName("userid")]
        public int UserID { get; set; } = 0;

        [JsonPropertyName("latitude")]
        public double Latitude { get; set; }

        [JsonPropertyName("longitude")]
        public double Longitude { get; set; }

        [JsonPropertyName("address")]
        public string Address { get; set; } = "";

        [JsonPropertyName("timestamp")]
        public DateTime Timestamp { get; set; } = DateTime.Now;

        [JsonPropertyName("accuracy")]
        public double Accuracy { get; set; }
    }
}
