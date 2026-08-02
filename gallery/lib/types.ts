export interface StyleData {
  no: number;
  styleCategory: string;
  type: string;
  keywords: string;
  primaryColors: string;
  secondaryColors: string;
  effectsAnimation: string;
  bestFor: string;
  doNotUseFor: string;
  lightMode: string;
  darkMode: string;
  performance: string;
  accessibility: string;
  mobileFriendly: string;
  conversionFocused: string;
  frameworkCompatibility: string;
  eraOrigin: string;
  complexity: string;
  aiPromptKeywords: string;
  cssTechnicalKeywords: string;
  implementationChecklist: string;
  designSystemVariables: string;
  // Computed fields
  extractedColors: string[];
  cssProperties: Record<string, string>;
}
