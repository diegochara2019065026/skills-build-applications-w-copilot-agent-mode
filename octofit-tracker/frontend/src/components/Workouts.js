import React, { useEffect, useState } from 'react';

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/workouts/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const items = data.results ? data.results : data;
        setWorkouts(items);
        console.log('Fetched workouts:', items);
        console.log('API endpoint:', apiUrl);
      })
      .catch(err => console.error('Error fetching workouts:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2 className="mb-4 display-6">Workouts</h2>
      <div className="table-responsive">
        <table className="table table-striped table-hover align-middle">
          <thead className="table-dark">
            <tr>
              <th>#</th>
              <th>Name</th>
              <th>Description</th>
              <th>Duration (min)</th>
            </tr>
          </thead>
          <tbody>
            {workouts.map((w, i) => (
              <tr key={i}>
                <td>{i + 1}</td>
                <td>{w.name}</td>
                <td>{w.description}</td>
                <td>{w.duration}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Workouts;
