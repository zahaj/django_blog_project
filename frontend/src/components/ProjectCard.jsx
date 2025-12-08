import TechBadge from './TechBadge';
import { useState } from 'react';

// We accept a 'project' object as a prop
function ProjectCard({ project }) {
  // Local state for this specific card
  const [likes, setLikes] = useState(0);

  const handleLike = () => {
    setLikes(likes + 1);
  };

  return (
    <div className="project-card">
      {project.image && (
        <img src={project.image} alt={project.title} width="200" />
      )}
      
      <h2>{project.title}</h2>
      <p>{project.description}</p>
      
      {/* Loop through technologies and use our new component */}
      <div className="tech-stack">
        {project.technologies.map(tech => (
          // We use the technology name as the key and prop
          <TechBadge key={tech} name={tech} />
        ))}
      </div>

      <button onClick={handleLike} style={{marginTop: '10px'}}>
        ❤️ {likes} Likes
      </button>
    </div>
  );
}

export default ProjectCard;