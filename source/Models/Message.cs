namespace StudentTracker.Models
{
    public class Message
    {
        int MessageID { get; set; }
        int SenderID { get; set; }
        int RecipientID { get; set; }

        public string RecipientType { get; set; }
        public string MessageContet { get; set; }

        public DateTime SentAt { get; set; } = DateTime.Now;
        public bool IsRead { get; set; } = false;
    }
}
