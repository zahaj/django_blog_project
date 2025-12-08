// A simple component to render a single technology tag
// It receives a string "name" as a prop
function TechBadge({ name }) {
  return (
    <span className="badge">
      {name}
    </span>
  );
}

export default TechBadge;