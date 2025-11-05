namespace StudentTracker.Models
{
    public class Message
    {
        public int ID { get; set; }
        public int SenderID { get; set; }
        public string SenderName { get; set; }
        public int RecipientID { get; set; }
        public string RecipientName { get; set; }

        public string RecipientType { get; set; }
        public string MessageContent { get; set; }

        public DateTime SentAt { get; set; } = DateTime.Now;
        public bool IsRead { get; set; } = false;
    }
}
