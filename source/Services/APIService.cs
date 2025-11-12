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
            _httpClient.BaseAddress = new Uri("http://127.0.0.1:8000/");
        }

        //User endpoints
        public async Task<string> CreateUserAsync(User user)
        {
            var response = await _httpClient.PostAsJsonAsync("users/", user);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStringAsync();
        }
        public async Task<User> GetUserByIdAsync(int id)
        {
            Console.WriteLine("Pinging API for a user");
            var response = await _httpClient.GetFromJsonAsync<User>($"users/{id}");
            return response;
        }

        public async Task<List<User>> GetUserAsync(string username, string password)
        {
            var response = await _httpClient.GetFromJsonAsync<List<User>>($"users/{username}/{password}");
            return response;
        }
        public async Task<List<User>> GetUsersAsync()
        {
            var response = await _httpClient.GetFromJsonAsync<List<User>>("users/");
            return response;
        }

        //Student endpoints
        public async Task<string> CreateStudentAsync(Student student)
        {
            var response = await _httpClient.PostAsJsonAsync("students/", student);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStringAsync();
        }
        public async Task<Student> GetStudentAsync(int id)
        {
            var response = await _httpClient.GetFromJsonAsync<Student>($"students/{id}");
            return response;
        }
        public async Task<List<Student>> GetStudentsAsync()
        {
            var response = await _httpClient.GetFromJsonAsync<List<Student>>("students/");
            return response;
        }

        //Instructor endpoints
        public async Task<string> CreateInstructorAsync(Instructor instructor)
        {
            var response = await _httpClient.PostAsJsonAsync("instructors/", instructor);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStringAsync();
        }
        public async Task<Instructor> GetInstructorAsync(int id)
        {
            var response = await _httpClient.GetFromJsonAsync<Instructor>($"instructors/{id}");
            return response;
        }
        public async Task<List<Instructor>> GetInstructorsAsync()
        {
            var response = await _httpClient.GetFromJsonAsync<List<Instructor>>("instructors/");
            return response;
        }

        //Messaging endpoints

        public async Task<string> CreateMessageAsync(Message message)
        {
            var response = await _httpClient.PostAsJsonAsync("messages/", message);
            Console.WriteLine(response);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStringAsync();
        }
        
        public async Task<Message> GetMessageAsync(int id)
        {
            var response = await _httpClient.GetFromJsonAsync<Message>($"messages/{id}");
            return response;
        }
        
        public async Task<List<Message>> GetMessagesAsync()
        {
            var response = await _httpClient.GetFromJsonAsync<List<Message>>("messages/");
            return response;
        }

        public async Task<List<Message>> GetMessagesToUserAsync(int idOfSender, int idOfRecipient)
        {
            var response = await _httpClient.GetFromJsonAsync<List<Message>>($"messages/{idOfSender}/{idOfRecipient}");
            return response;
        }
        public async Task<List<Message>> GetMessagesByUserAsync(int userId)
        {
            var response = await _httpClient.GetFromJsonAsync<List<Message>>($"messages/{userId}");
            return response;
        }
        public async Task<string> CreateLocationAsync(Location location)
        {
            var response = await _httpClient.PostAsJsonAsync("location/", location);
            Console.WriteLine(response);
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStringAsync();
        }


    }
}
