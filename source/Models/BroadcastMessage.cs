namespace StudentTracker.Models
{
    public class BroadcastMessage
    {
        public string BroadcastID { get; set; }

        public string InstructorID { get; set; }

        public string CourseID { get; set; }

        public string Message { get; set; }

        public DateOnly SentAt { get; set; }

        public int recipientCount { get; set; }

    }
}
