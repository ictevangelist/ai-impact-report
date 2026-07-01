/* =====================================================================
   Data & Findings charts — Woodland Academy Trust AI Review
   All data values are hard-coded from the report. No external API calls;
   the charting library and data-label plugin are vendored locally.
   Every bar carries a printed value so changes to 0% remain readable.
   ===================================================================== */
(function () {
  if (typeof Chart === 'undefined') {
    console.warn('Chart.js not loaded — see the data table for all figures.');
    return;
  }
  if (typeof ChartDataLabels !== 'undefined') {
    Chart.register(ChartDataLabels);
  }

  var BASELINE = '#8a99a3';   // slate — baseline (before AI)
  var FOLLOWUP = '#0ea3ab';   // brand teal — follow-up (after AI)
  var INCLUSION= '#0ea3ab';   // brand teal — inclusion outcomes
  var GRID     = 'rgba(21,32,43,.08)';
  var TICK     = '#45525d';
  var LABEL    = '#15202b';

  Chart.defaults.font.family = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif";
  Chart.defaults.font.size = 13;
  Chart.defaults.color = TICK;

  function legend() {
    return { position: 'top', labels: { boxWidth: 14, padding: 16, font: { size: 13 } } };
  }
  // Value label sitting just above each vertical bar (shows even for 0).
  function pctLabelTop() {
    return {
      anchor: 'end', align: 'end', offset: 0, clamp: true,
      color: LABEL, font: { weight: '600', size: 12 },
      formatter: function (v) { return v + '%'; }
    };
  }
  function hrsLabelTop() {
    return {
      anchor: 'end', align: 'end', offset: 0, clamp: true,
      color: LABEL, font: { weight: '600', size: 12 },
      formatter: function (v) { return v; }
    };
  }

  /* ---- Chart 1: Weekly planning time (hours) — baseline vs follow-up ---- */
  new Chart(document.getElementById('chartPlanningTime'), {
    type: 'bar',
    data: {
      labels: ['Average', 'Median', 'Maximum'],
      datasets: [
        { label: 'Baseline (Nov 2024)', data: [10, 7, 24], backgroundColor: BASELINE, borderRadius: 5 },
        { label: 'Follow-up (Feb 2025)', data: [4.75, 4, 10], backgroundColor: FOLLOWUP, borderRadius: 5 }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      layout: { padding: { top: 18 } },
      plugins: {
        legend: legend(),
        datalabels: hrsLabelTop(),
        tooltip: { callbacks: { label: function (c) { return c.dataset.label + ': ' + c.parsed.y + ' hrs'; } } }
      },
      scales: {
        y: { beginAtZero: true, title: { display: true, text: 'Hours per week' }, grid: { color: GRID } },
        x: { grid: { display: false } }
      }
    }
  });

  /* ---- Chart 2: Planning efficiency, confidence, fit, adaptability (%) ---- */
  new Chart(document.getElementById('chartConfidence'), {
    type: 'bar',
    data: {
      labels: [['Rated efficient /', 'very efficient'], ['Teacher planning', 'confidence'], ['Planning meets', 'class needs'], ['SEND / EAL', 'adaptability']],
      datasets: [
        { label: 'Baseline', data: [0, 50, 37.5, 50], backgroundColor: BASELINE, borderRadius: 5 },
        { label: 'Follow-up', data: [88, 100, 100, 88], backgroundColor: FOLLOWUP, borderRadius: 5 }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      layout: { padding: { top: 18 } },
      plugins: {
        legend: legend(),
        datalabels: pctLabelTop(),
        tooltip: { callbacks: { label: function (c) { return c.dataset.label + ': ' + c.parsed.y + '%'; } } }
      },
      scales: {
        y: { beginAtZero: true, max: 100, title: { display: true, text: '% of staff' },
             ticks: { callback: function (v) { return v + '%'; } }, grid: { color: GRID } },
        x: { grid: { display: false }, ticks: { maxRotation: 0, autoSkip: false } }
      }
    }
  });

  /* ---- Chart 3: Workload & wellbeing — full shift, baseline vs follow-up ---- */
  /* Shows both the fall in negative measures and the matching rise in the
     positive one, so every bar (and the drop to 0%) is visible and labelled. */
  new Chart(document.getElementById('chartWellbeing'), {
    type: 'bar',
    data: {
      labels: [
        ['Planning is a', 'HIGH burden on workload'],
        ['Planning is a', 'LOW burden on workload'],
        ['Often / always', 'overwhelmed by planning']
      ],
      datasets: [
        { label: 'Baseline', data: [75, 0, 75], backgroundColor: BASELINE, borderRadius: 5 },
        { label: 'Follow-up', data: [0, 75, 0], backgroundColor: FOLLOWUP, borderRadius: 5 }
      ]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      layout: { padding: { top: 18 } },
      plugins: {
        legend: legend(),
        datalabels: pctLabelTop(),
        tooltip: { callbacks: { label: function (c) { return c.dataset.label + ': ' + c.parsed.y + '%'; } } }
      },
      scales: {
        y: { beginAtZero: true, max: 100, title: { display: true, text: '% of staff' },
             ticks: { callback: function (v) { return v + '%'; } }, grid: { color: GRID } },
        x: { grid: { display: false }, ticks: { maxRotation: 0, autoSkip: false } }
      }
    }
  });

  /* ---- Chart 4: Inclusion outcomes (% reporting at follow-up) — horizontal ---- */
  new Chart(document.getElementById('chartInclusion'), {
    type: 'bar',
    data: {
      labels: [
        ['Faster, better', 'differentiated materials'],
        ['KS2 pupils preferred', 'AI-supported lessons'],
        ['More equitable access', '(without lowering the bar)'],
        ['Increased pupil', 'engagement'],
        ['Improved learner', 'independence']
      ],
      datasets: [
        { label: '% reporting', data: [95, 91, 89, 82, 78], backgroundColor: INCLUSION, borderRadius: 5, barThickness: 26 }
      ]
    },
    options: {
      indexAxis: 'y',
      responsive: true, maintainAspectRatio: false,
      layout: { padding: { right: 14 } },
      plugins: {
        legend: { display: false },
        datalabels: {
          anchor: 'end', align: 'start', offset: 8, clamp: true,
          color: '#ffffff', font: { weight: '700', size: 12 },
          formatter: function (v) { return v + '%'; }
        },
        tooltip: { callbacks: { label: function (c) { return c.parsed.x + '%'; } } }
      },
      scales: {
        x: { beginAtZero: true, max: 100, title: { display: true, text: '% reporting (follow-up)' },
             ticks: { callback: function (v) { return v + '%'; } }, grid: { color: GRID } },
        y: { grid: { display: false }, ticks: { autoSkip: false, font: { size: 12.5 } } }
      }
    }
  });
})();
