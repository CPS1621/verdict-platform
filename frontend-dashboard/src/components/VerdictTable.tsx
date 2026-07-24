interface Verdict {
  id: number;
  rule_name: string;
  verdict: string;
  created_at: string;
}

interface VerdictTableProps {
  verdicts: Verdict[];
}

function VerdictTable({ verdicts }: VerdictTableProps) {
  return (
    <table
      style={{
        width: "100%",
        borderCollapse: "collapse",
        marginTop: "20px",
      }}
    >
      <thead>
        <tr>
          <th style={{ border: "1px solid #ddd", padding: "12px" }}>ID</th>
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
  );
}

export default VerdictTable;