interface VerdictFilterProps {
  selectedStatus: string;
  onStatusChange: (status: string) => void;
}

function VerdictFilter({
  selectedStatus,
  onStatusChange,
}: VerdictFilterProps) {
  return (
    <div style={{ marginBottom: "20px" }}>
      <label style={{ marginRight: "10px", fontWeight: "bold" }}>
        Filter by Status:
      </label>

      <select
        value={selectedStatus}
        onChange={(e) => onStatusChange(e.target.value)}
        style={{
          padding: "8px",
          borderRadius: "5px",
        }}
      >
        <option value="All">All</option>
        <option value="Detected">Detected</option>
        <option value="Missed">Missed</option>
        <option value="Partial">Partial</option>
        <option value="No Data">No Data</option>
      </select>
    </div>
  );
}

export default VerdictFilter;