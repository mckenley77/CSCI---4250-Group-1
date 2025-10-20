namespace StudentTracker.Models
{
    public class Student
    {
        public int StudentID { get; set; }

        public string Major { get; set; } = string.Empty;

        public DateTime EnrollmentDate { get; set; }

        public bool LocationSharingEnabled { get; set; }

        List<Course> EnrolledCourses { get; set; } = new List<Course>();


    }
}
