import { StyleData } from "./types";
import { extractColors } from "./colorExtractor";
import { parseCssKeywords } from "./cssGenerator";

function parseCSVLine(line: string): string[] {
  const fields: string[] = [];
  let current = "";
  let inQuotes = false;

  for (let i = 0; i < line.length; i++) {
    const char = line[i];
    if (inQuotes) {
      if (char === '"') {
        if (i + 1 < line.length && line[i + 1] === '"') {
          current += '"';
          i++;
        } else {
          inQuotes = false;
        }
      } else {
        current += char;
      }
    } else {
      if (char === '"') {
        inQuotes = true;
      } else if (char === ",") {
        fields.push(current.trim());
        current = "";
      } else {
        current += char;
      }
    }
  }
  fields.push(current.trim());
  return fields;
}

export function parseStylesCSV(csvContent: string): StyleData[] {
  const lines = csvContent.split("\n").filter((l) => l.trim().length > 0);
  if (lines.length < 2) return [];

  // Skip header
  const dataLines = lines.slice(1);
  return dataLines.map((line) => {
    const f = parseCSVLine(line);
    const primaryColors = f[4] || "";
    const secondaryColors = f[5] || "";
    const cssTechnicalKeywords = f[19] || "";

    return {
      no: parseInt(f[0]) || 0,
      styleCategory: f[1] || "",
      type: f[2] || "",
      keywords: f[3] || "",
      primaryColors,
      secondaryColors,
      effectsAnimation: f[6] || "",
      bestFor: f[7] || "",
      doNotUseFor: f[8] || "",
      lightMode: f[9] || "",
      darkMode: f[10] || "",
      performance: f[11] || "",
      accessibility: f[12] || "",
      mobileFriendly: f[13] || "",
      conversionFocused: f[14] || "",
      frameworkCompatibility: f[15] || "",
      eraOrigin: f[16] || "",
      complexity: f[17] || "",
      aiPromptKeywords: f[18] || "",
      cssTechnicalKeywords,
      implementationChecklist: f[20] || "",
      designSystemVariables: f[21] || "",
      extractedColors: extractColors(`${primaryColors} ${secondaryColors}`),
      cssProperties: parseCssKeywords(cssTechnicalKeywords),
    };
  });
}
