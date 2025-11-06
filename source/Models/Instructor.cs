using System.Text.Json.Serialization;

namespace StudentTracker.Models
{
    public class Instructor : User 
    {
        [JsonPropertyName("instructorid")]
        public int InstructorID { get; set; }

        [JsonPropertyName("department")]
        public string Department { get; set; }

        [JsonIgnore]
        public List<Course> TaughtCourses { get; set; } = new List<Course>();
    }
}
