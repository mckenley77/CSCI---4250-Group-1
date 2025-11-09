using System.Text.Json.Serialization;

namespace StudentTracker.Models
{
    public class Student : User
    {
        [JsonPropertyName("studentid")]
        public int StudentID { get; set; }

        [JsonPropertyName("major")]

        public string Major { get; set; } = string.Empty;

        [JsonPropertyName("locationsharingenabled")]
        public bool LocationSharingEnabled { get; set; }

        [JsonIgnore]
        List<Course> EnrolledCourses { get; set; } = new List<Course>();


    }
}
