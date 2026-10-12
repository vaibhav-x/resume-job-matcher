


















## Known Limitations
- Section detection relies on common resume header phrasing. Resumes using 
  non-standard headers may not be fully captured.
- When a resume combines multiple categories under one header (e.g. 
  "Internships & Live Projects"), the same content is duplicated across 
  both the Experience and Projects sections, since there's no reliable 
  way to split combined content without deeper NLP.