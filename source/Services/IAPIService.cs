using StudentTracker.Models;

namespace StudentTracker.Services
{
    public interface IAPIService
    {
        public User CurrentUser { get; set; }

        Task<string> CreateUserAsync(User user);

        Task<User> GetUserAsync(string username, string password);
    }
}
