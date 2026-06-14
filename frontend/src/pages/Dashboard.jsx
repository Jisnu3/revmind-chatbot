import { useEffect, useState } from "react";
import API from "../api/api";
import KPICard from "../components/KPICard";
import RevenueChart from "../components/RevenueChart";

function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [trends, setTrends] = useState([]);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      const summaryRes = await API.get("/api/summary");
      const trendsRes = await API.get("/api/trends");

      setSummary(summaryRes.data);
      setTrends(trendsRes.data);
    } catch (err) {
      console.error(err);
    }
  };

  if (!summary) return <h2>Loading Dashboard...</h2>;

  return (
    <div className="dashboard">
      <h1>NovaBite Sales Dashboard</h1>

      <div className="kpi-grid">
        <KPICard
          title="Total Revenue"
          value={`$${summary.total_net_revenue.toLocaleString()}`}
        />

        <KPICard
          title="Gross Profit Margin"
          value={`${summary.gross_profit_margin}%`}
        />

        <KPICard
          title="Top Region"
          value={summary.top_region}
        />
      </div>

      <RevenueChart data={trends} />
    </div>
  );
}

export default Dashboard;