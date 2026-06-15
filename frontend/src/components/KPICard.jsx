function KPICard({ title, value, icon, type }) {
  return (
    <div className="kpi-card">
      <div className={`kpi-icon ${type}`}>
        {icon}
      </div>

      <div>
        <h3>{title}</h3>
        <p>{value}</p>
      </div>
    </div>
  );
}

export default KPICard;