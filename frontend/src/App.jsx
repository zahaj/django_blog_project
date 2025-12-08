import { useState, useEffect } from 'react'
import Layout from './components/Layout';
import ProjectCard from './components/ProjectCard';
import './App.css'

function App() {
  const [projects, setProjects] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch from Neon/Render backend via local Docker proxy
    // OR directly from the URL if CORS is set up.
    // Let's assume running Docker locally for now:
    fetch('http://127.0.0.1:8000/api/projects/')
      .then(response => {
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
      })
      .then(data => {
        setProjects(data);
        setIsLoading(false);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
        setError(error.message);
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return (
      <h2>🌀 Loading projects...</h2>
    );
  }

  if (error) {
    return (
      <Layout>
        <h2 style={{color: 'red'}}>⚠️ Error loading portfolio</h2>
        <p>{error}</p>
      </Layout>
    );
  }

  return (
    <Layout>
      <div className="project-list">
        {projects.map(project => (
          // Pass the data down to the child component
          <ProjectCard key={project.id} project={project} />
        ))}
      </div>
    </Layout>
  );
}

export default App