namespace StudentTracker.Models
{
    public class Student : User
    {
        public int StudentID { get; set; }

        public string Major { get; set; } = string.Empty;

        public DateOnly EnrollmentDate { get; set; }

        public bool LocationSharingEnabled { get; set; }

        List<Course> EnrolledCourses { get; set; } = new List<Course>();


    }
}
