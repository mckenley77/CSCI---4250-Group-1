using StudentTracker.Models;

namespace StudentTracker.Services
{
    public class APIService : IAPIService
    {
        private readonly HttpClient _httpClient;

        public Action OnUserChanged { get; set; }

        //To be used in .razor pages!
        private User _currentUser;
        public User CurrentUser
        {
            get => _currentUser;
            set
            {
                if (_currentUser != value)
                {
                    _currentUser = value;
                    OnUserChanged?.Invoke();
                }
            }
        }

        public APIService()
        {
            _httpClient = new HttpClient();
            _httpClient.BaseAddress = new Uri("http://localhost:8000/");
        }

        public async Task<string> CreateUserAsync(User user)
        {
            var response = await _httpClient.PostAsJsonAsync("users/", user);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStringAsync();
        }

        public async Task<User> GetUserAsync(string username, string password)
        {
            var response = await _httpClient.GetFromJsonAsync<User>($"users/{username}/{password}");
            return response;
        }
    }
}
