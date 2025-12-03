import { useState, useEffect } from 'react'
import './App.css'

// A reusable component for a Like Button
function LikeButton() {
  // Define State: 'likes' starts at 0
  const [likes, setLikes] = useState(0);

  // Define the Click Handler
  const handleClick = () => {
    setLikes(likes + 1);
  };

  // Render the HTML
  return (
    <button onClick={handleClick}>
      ❤️ {likes} Likes
    </button>
  );
}

// A reusable component for a Is Liked Button
function IsLikedButton() {
  const [isLiked, setIsLiked] = useState(false)
  const handleClick = () => {
    setIsLiked(!isLiked);
  };

  return (
    <button onClick={handleClick}>
      {isLiked ? "❤️ Liked!" : "🤍 Like"}
    </button>
  );
}

function App() {
  // 1. useState: "Memory" for our component.
  // We start with an empty list of projects.
  const [projects, setProjects] = useState([])

  // 2. useEffect: "Action" to take when the page loads.
  useEffect(() => {
    // Fetch data from your LOCAL Django Docker API
    fetch('http://127.0.0.1:8000/api/projects/')
      .then(response => response.json())
      .then(data => {
        console.log(data); // Check your browser console!
        setProjects(data); // Save the data to state
      })
      .catch(error => console.error('Error fetching data:', error));
  }, [])

  return (
    <div className="app-container">
      <h1>My React Portfolio</h1>
      
      <div className="project-list">
        {/* 3. Loop through the projects and render them */}
        {projects.map(project => (
          <div key={project.id} className="project-card">
            {project.image && <img src={project.image} alt={project.title} width="200" />}
            <h2>{project.title}</h2>
            <p>{project.description}</p>
            <small>{project.technologies.join(", ")}</small>
            <div style={{ marginTop: '10px' }}>
              <IsLikedButton />
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default App