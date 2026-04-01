import React, { useEffect, useState } from 'react';

const getApiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  return codespace
    ? `https://${codespace}-8000.app.github.dev/api/teams/`
    : '/api/teams/';
};

export default function Teams() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const url = getApiUrl();
    console.log('Fetching Teams from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Teams data:', results);
      });
  }, []);
  return (
    <div>
      <h2>Teams</h2>
      <ul>
        {data.map((t, i) => (
          <li key={i}>{t._id} - {t.name}</li>
        ))}
      </ul>
    </div>
  );
}
