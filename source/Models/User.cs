﻿using System.Data.SqlTypes;
using System.Security.Cryptography;
using System.Text;
using System.Text.Json.Serialization;

namespace StudentTracker.Models
{
    /// <summary>
    /// Represents a user of the application
    /// </summary>
    public class User
    {
        [JsonPropertyName("id")]
        public int Id { get; set; }

        [JsonPropertyName("username")]
        public string Username { get; set; }

        /// <summary>
        /// User's Password. Is hashed when stored in the database, and logins
        /// are checked against the hash
        /// </summary>

        [JsonPropertyName ("password")]
        private string Password { get; set; }

        private string UserSalt { get; set; } 

        [JsonPropertyName("firstname")]
        public string FirstName { get; set; }

        [JsonPropertyName("lastname")]
        public string LastName { get; set; }

        public string Email { get; set; }
        private string PhoneNum { get; set; }

        private DateTime CreatedAt = DateTime.Now;
        
        public bool IsActive { get; set; }

        //public User()
        //{
        //    byte[] UserSaltBytes = new byte[16];
        //    using(var rng = RandomNumberGenerator.Create())
        //    {
        //        rng.GetBytes(UserSaltBytes);
        //    }
        //    string salt = Convert.ToBase64String(UserSaltBytes );
        //
        //    HashPassword(Password, UserSaltBytes);
        //}


        //Working on password hashing, but primitive login will be with just plaintext. 
       // public void HashPassword(string toBeHashed, byte[] SaltBytes)
       // {
       //     byte[] passwordBytes = Encoding.UTF8.GetBytes(toBeHashed);
       //     byte[] saltedPasswordBytes = new byte[passwordBytes.Length + SaltBytes.Length];
       //
       //     Buffer.BlockCopy(passwordBytes, 0, saltedPasswordBytes, 0, passwordBytes.Length);
       //     Buffer.BlockCopy(SaltBytes, 0, saltedPasswordBytes, passwordBytes.Length, SaltBytes.Length);
       // }
    }
}
