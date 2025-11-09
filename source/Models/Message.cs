using System.Text.Json.Serialization;

namespace StudentTracker.Models
{
    public class Message
    {
        [JsonPropertyName("messageid")]
        public int MessageID { get; set; }

        [JsonPropertyName("senderId")]
        public int SenderID { get; set; }

        [JsonPropertyName("sendername")]
        public string SenderName { get; set; }

        [JsonPropertyName("recipientid")]
        public int RecipientID { get; set; }

        [JsonPropertyName("recipientname")]
        public string RecipientName { get; set; }

        [JsonPropertyName("recipienttype")]
        public string RecipientType { get; set; }

        [JsonPropertyName("messagecontent")]
        public string MessageContent { get; set; }

        [JsonPropertyName("isread")]
        public bool IsRead { get; set; } = false;
    }
}
