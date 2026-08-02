import { StyleData } from "@/lib/types";

interface MetadataBadgesProps {
  style: StyleData;
}

function Badge({
  label,
  variant,
}: {
  label: string;
  variant: "green" | "yellow" | "red" | "blue" | "gray";
}) {
  const colors = {
    green: "bg-green-100 text-green-800 dark:bg-green-900/30 dark:text-green-400",
    yellow: "bg-yellow-100 text-yellow-800 dark:bg-yellow-900/30 dark:text-yellow-400",
    red: "bg-red-100 text-red-800 dark:bg-red-900/30 dark:text-red-400",
    blue: "bg-blue-100 text-blue-800 dark:bg-blue-900/30 dark:text-blue-400",
    gray: "bg-gray-100 text-gray-700 dark:bg-gray-800 dark:text-gray-400",
  };

  return (
    <span className={`inline-flex items-center px-2 py-0.5 text-[10px] font-medium rounded-full ${colors[variant]}`}>
      {label}
    </span>
  );
}

function getComplexityVariant(c: string): "green" | "yellow" | "red" {
  if (c === "Low") return "green";
  if (c === "Medium") return "yellow";
  return "red";
}

function getPerfVariant(p: string): "green" | "yellow" | "red" {
  if (p.includes("Excellent")) return "green";
  if (p.includes("Good")) return "yellow";
  return "red";
}

function getA11yVariant(a: string): "green" | "yellow" | "red" {
  if (a.includes("AAA")) return "green";
  if (a.includes("AA") || a.includes("Good")) return "yellow";
  return "red";
}

export function MetadataBadges({ style }: MetadataBadgesProps) {
  return (
    <div className="flex flex-wrap gap-1.5">
      <Badge label={style.complexity} variant={getComplexityVariant(style.complexity)} />
      <Badge label={style.performance.replace(/[⚡❌⚠]/g, "").trim()} variant={getPerfVariant(style.performance)} />
      <Badge label={style.accessibility.replace(/[✓⚠✗]/g, "").trim()} variant={getA11yVariant(style.accessibility)} />
      {style.lightMode.includes("Full") && <Badge label="Light" variant="blue" />}
      {style.darkMode.includes("Full") && <Badge label="Dark" variant="gray" />}
    </div>
  );
}
