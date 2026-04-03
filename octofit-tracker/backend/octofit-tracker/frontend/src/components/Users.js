import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const apiUrl = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        const items = data.results ? data.results : data;
        setUsers(items);
        console.log('Fetched users:', items);
        console.log('API endpoint:', apiUrl);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, [apiUrl]);

  return (
    <div className="container mt-4">
      <h2>Users</h2>
      <ul className="list-group">
        {users.map((u, i) => (
          <li key={i} className="list-group-item">
            {u.username} - {u.email} - {u.team_name}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Users;
