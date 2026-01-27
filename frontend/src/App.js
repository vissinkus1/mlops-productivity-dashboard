import { useEffect, useState } from "react";

function App() {
  const [factory, setFactory] = useState(null);
  const [workers, setWorkers] = useState([]);
  const [stations, setStations] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/metrics/factory")
      .then(res => res.json())
      .then(data => setFactory(data));

    fetch("http://127.0.0.1:8000/metrics/workers")
      .then(res => res.json())
      .then(data => setWorkers(data));

    fetch("http://127.0.0.1:8000/metrics/workstations")
      .then(res => res.json())
      .then(data => setStations(data));
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>AI Worker Productivity Dashboard</h1>

      {factory && (
        <>
          <h2>Factory Summary</h2>
          <p>Total Productive Minutes: {factory.total_productive_minutes}</p>
          <p>Total Units Produced: {factory.total_units_produced}</p>
          <p>Average Utilization: {factory.average_utilization_percent}%</p>
          <p>Avg Production Rate/hr: {factory.average_production_rate_per_hour}</p>
        </>
      )}

      <h2>Workers</h2>
      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Worker</th>
            <th>Working (min)</th>
            <th>Idle (min)</th>
            <th>Utilization %</th>
            <th>Units</th>
            <th>Units/hr</th>
          </tr>
        </thead>
        <tbody>
          {workers.map(w => (
            <tr key={w.worker_id}>
              <td>{w.worker_id}</td>
              <td>{w.working_minutes}</td>
              <td>{w.idle_minutes}</td>
              <td>{w.utilization_percent}</td>
              <td>{w.units_produced}</td>
              <td>{w.units_per_hour}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Workstations</h2>
      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Station</th>
            <th>Occupied (min)</th>
            <th>Units</th>
            <th>Throughput/hr</th>
          </tr>
        </thead>
        <tbody>
          {stations.map(s => (
            <tr key={s.workstation_id}>
              <td>{s.workstation_id}</td>
              <td>{s.occupied_minutes}</td>
              <td>{s.units_produced}</td>
              <td>{s.throughput_per_hour}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;

