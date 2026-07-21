import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

interface Verdict {
  id: number;
  rule_name: string;
  verdict: string;
  created_at: string;
}

function Dashboard() {
  const [verdicts, setVerdicts] = useState<Verdict[]>([]);
  const [loading, setLoading] = useState(true);

  const navigate = useNavigate();

  useEffect(() => {
    api
      .get("/verdicts")
      .then((response) => {
        setVerdicts(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching verdicts:", error);
        setLoading(false);
      });
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  const detectedCount = verdicts.filter(
    (v) => v.verdict === "Detected"
  ).length;

  const missedCount = verdicts.filter(
    (v) => v.verdict === "Missed"
  ).length;

  const partialCount = verdicts.filter(
    (v) => v.verdict === "Partial"
  ).length;

  return (
    <div style={{ padding: "30px" }}>
      <h1>CyBreach Validator Dashboard</h1>

      <button
        onClick={handleLogout}
        style={{
          marginBottom: "20px",
          padding: "8px 16px",
          cursor: "pointer",
        }}
      >
        Logout
      </button>

      {/* Summary Cards */}
      <div
        style={{
          display: "flex",
          gap: "20px",
          marginBottom: "30px",
          flexWrap: "wrap",
        }}
      >
        <div
          style={{
            border: "1px solid #ccc",
            borderRadius: "8px",
            padding: "20px",
            width: "180px",
            backgroundColor: "#f8f9fa",
          }}
        >
          <h3>Total Verdicts</h3>
          <h1>{verdicts.length}</h1>
        </div>

        <div
          style={{
            border: "1px solid green",
            borderRadius: "8px",
            padding: "20px",
            width: "180px",
            backgroundColor: "#f0fff4",
          }}
        >
          <h3>Detected</h3>
          <h1 style={{ color: "green" }}>{detectedCount}</h1>
        </div>

        <div
          style={{
            border: "1px solid red",
            borderRadius: "8px",
            padding: "20px",
            width: "180px",
            backgroundColor: "#fff5f5",
          }}
        >
          <h3>Missed</h3>
          <h1 style={{ color: "red" }}>{missedCount}</h1>
        </div>

        <div
          style={{
            border: "1px solid orange",
            borderRadius: "8px",
            padding: "20px",
            width: "180px",
            backgroundColor: "#fffaf0",
          }}
        >
          <h3>Partial</h3>
          <h1 style={{ color: "orange" }}>{partialCount}</h1>
        </div>
      </div>

      <h2>Verdicts</h2>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <table
          style={{
            width: "100%",
            borderCollapse: "collapse",
            marginTop: "20px",
          }}
        >
          <thead>
            <tr>
              <th style={{ border: "1px solid #ddd", padding: "12px" }}>
                ID
              </th>
              <th style={{ border: "1px solid #ddd", padding: "12px" }}>
                Rule Name
              </th>
              <th style={{ border: "1px solid #ddd", padding: "12px" }}>
                Verdict
              </th>
              <th style={{ border: "1px solid #ddd", padding: "12px" }}>
                Created At
              </th>
            </tr>
          </thead>

          <tbody>
            {verdicts.map((verdict) => (
              <tr key={verdict.id}>
                <td style={{ border: "1px solid #ddd", padding: "10px" }}>
                  {verdict.id}
                </td>

                <td style={{ border: "1px solid #ddd", padding: "10px" }}>
                  {verdict.rule_name}
                </td>

                <td style={{ border: "1px solid #ddd", padding: "10px" }}>
                  <span
                    style={{
                      color:
                        verdict.verdict === "Detected"
                          ? "green"
                          : verdict.verdict === "Missed"
                          ? "red"
                          : verdict.verdict === "Partial"
                          ? "orange"
                          : "gray",
                      fontWeight: "bold",
                    }}
                  >
                    {verdict.verdict}
                  </span>
                </td>

                <td style={{ border: "1px solid #ddd", padding: "10px" }}>
                  {new Date(verdict.created_at).toLocaleString()}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default Dashboard;