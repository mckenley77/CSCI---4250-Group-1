namespace StudentTracker.Models
{
    public class Instructor : User
    {
        public int InstructorID { get; set; }

        public string Department { get; set; }

        public List<Course> TaughtCourses { get; set; } = new List<Course>();
    }
}
