import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../services/api";

interface Verdict {
  id: number;
  rule_id: number;
  rule_name: string;
  verdict: string;
  event_data: string;
  created_at: string;
}

function VerdictDetails() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [verdict, setVerdict] = useState<Verdict | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api
      .get(`/verdicts/${id}`)
      .then((response) => {
        setVerdict(response.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching verdict:", error);
        setLoading(false);
      });
  }, [id]);

  if (loading) {
    return <p>Loading verdict details...</p>;
  }

  if (!verdict) {
    return <p>Verdict not found.</p>;
  }

  return (
    <div style={{ padding: "30px" }}>
      <h1>Verdict Details</h1>

      <button
        onClick={() => navigate("/dashboard")}
        style={{
          marginBottom: "20px",
          padding: "8px 16px",
          cursor: "pointer",
        }}
      >
        Back to Dashboard
      </button>

      <div
        style={{
          border: "1px solid #ccc",
          borderRadius: "8px",
          padding: "20px",
          maxWidth: "700px",
        }}
      >
        <p><strong>ID:</strong> {verdict.id}</p>

        <p><strong>Rule ID:</strong> {verdict.rule_id}</p>

        <p><strong>Rule Name:</strong> {verdict.rule_name}</p>

        <p><strong>Verdict:</strong> {verdict.verdict}</p>

        <p><strong>Created At:</strong> {new Date(verdict.created_at).toLocaleString()}</p>

        <p><strong>Event Data:</strong></p>

        <pre
           style={{
              background: "#f4f4f4",
              padding: "15px",
              borderRadius: "5px",
              overflowX: "auto",
            }}
          >
            {JSON.stringify(JSON.parse(verdict.event_data), null, 2)}
         </pre>
      </div>
    </div>
  );
}

export default VerdictDetails;