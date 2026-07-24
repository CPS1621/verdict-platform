interface StatusBadgeProps {
  verdict: string;
}

function StatusBadge({ verdict }: StatusBadgeProps) {
  const getColor = () => {
    switch (verdict) {
      case "Detected":
        return "green";

      case "Missed":
        return "red";

      case "Partial":
        return "orange";

      default:
        return "gray";
    }
  };

  return (
    <span
      style={{
        color: getColor(),
        fontWeight: "bold",
      }}
    >
      {verdict}
    </span>
  );
}

export default StatusBadge;