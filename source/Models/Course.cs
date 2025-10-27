namespace StudentTracker.Models
{
    public class Course
    {
        public int CourseID { get; set; }

        public string CourseName { get; set; }

        public string CourseCode { get; set; }

        public string CourseDescription { get; set; }

        public DateOnly StartDate { get; set; }
        public DateOnly EndDate { get; set; }

    }
}
