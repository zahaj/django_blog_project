import Layout from './components/Layout';
import ProjectCard from './components/ProjectCard';
import useProjects from './hooks/useProjects';
import './App.css'

function App() {

  const { projects, isLoading, error, refresh } = useProjects();
  
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
      <div style={{ marginTop: '20px', textAlign: 'center' }}>
        <button onClick={refresh} className="btn-refresh">
          🔄 Refresh Data
        </button>
      </div>
    </Layout>
  );
}

export default App;