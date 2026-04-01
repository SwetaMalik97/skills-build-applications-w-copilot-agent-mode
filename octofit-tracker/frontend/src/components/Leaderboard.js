import React, { useEffect, useState } from 'react';

const getApiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  return codespace
    ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
    : '/api/leaderboard/';
};

export default function Leaderboard() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const url = getApiUrl();
    console.log('Fetching Leaderboard from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Leaderboard data:', results);
      });
  }, []);
  return (
    <div>
      <h2>Leaderboard</h2>
      <ul>
        {data.map((l, i) => (
          <li key={i}>{l.team} - {l.points} pts</li>
        ))}
      </ul>
    </div>
  );
}
