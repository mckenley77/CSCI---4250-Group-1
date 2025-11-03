using StudentTracker.Models;
using System.Net.Http;

namespace StudentTracker.Services
{
    public interface IAPIService
    {
        public User CurrentUser { get; set; }

        Task<string> CreateUserAsync(User user);

        Task<List<User>> GetUserAsync(string username, string password);

        Task<User> GetUserByIdAsync(int id);

        //Student endpoints
        Task<string> CreateStudentAsync(Student student);

        Task<Student> GetStudentAsync(int id);

        Task<List<Student>> GetStudentsAsync();


        //Instructor endpoints
        Task<string> CreateInstructorAsync(Instructor instructor);

        Task<Instructor> GetInstructorAsync(int id);

        Task<List<Instructor>> GetInstructorAsync();


        //Messaging endpoints

        Task<string> CreateMessageAsync(Message message);


        Task<Message> GetMessageAsync(int id);


        Task<List<Message>> GetMessagesAsync();


        Task<List<Message>> GetMessagesToUserAsync(int senderId, int recipientId);

        Task<List<Message>> GetMessagesByUserAsync(int userId);
        
    }
}
