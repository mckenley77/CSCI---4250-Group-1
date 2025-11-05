namespace StudentTracker.Models
{
    public class Message
    {
        int MessageID { get; set; }
        public int SenderID { get; set; }
        public string SenderName { get; set; }
        public int RecipientID { get; set; }
        public string RecipientName { get; set; }

        public string RecipientType { get; set; }
        public string MessageContet { get; set; }

        public DateTime SentAt { get; set; } = DateTime.Now;
        public bool IsRead { get; set; } = false;
    }
}
