import { useState, useEffect } from 'react';

const API_BASE_URL = import.meta.env.VITE_API_URL;

function useProjects() {
  const [projects, setProjects] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // 1. Define the fetch logic as a standalone function
  const fetchProjects = async () => {
    setIsLoading(true); // Show loading spinner again while refreshing
    setError(null);     // Clear any old errors
    try {
      const response = await fetch(`${API_BASE_URL}/api/projects/`);
      
      if (!response.ok) {
        throw new Error(`API call failed with status: ${response.status}`);
      }
      
      const data = await response.json();
      setProjects(data);
    } catch (err) {
      console.error('Error fetching data:', err);
      setError(err.message || 'Could not connect to the backend server.');
    } finally {
      setIsLoading(false); // Stop loading (whether success or fail)
    }
  };

  // 2. Use useEffect to call it ONCE when the component mounts
  useEffect(() => {
    fetchProjects();
  }, []);

  // 3. Return the function as 'refresh' so App.jsx can use it
  return { projects, isLoading, error, refresh: fetchProjects };
}

export default useProjects;