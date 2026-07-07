# claude-routine-european-grants

Daily monitor for EU funding opportunities (Erasmus+, Horizon Europe, Digital Europe) — Claude Code cloud routine.

## What it does

This Claude Code cloud routine runs daily and:

1. Searches for new or updated EU funding calls published in the last 24–48 hours, relevant to a **public-private consortium** (school + private company) working on AI, coding, digital skills, and teacher/student training
2. Flags calls with deadlines approaching within 30 days
3. Sends a bilingual summary email (English + Italian) to the consortium team

## Monitored programmes

| Programme | Focus |
|---|---|
| Erasmus+ | Cooperation Partnerships, Teacher Academies, Digital Education |
| Horizon Europe | Digital, Industry & Space cluster; Civil Society pillar |
| Digital Europe Programme (DIGITAL) | Advanced digital skills |
| Creative Europe | Educational/media content (when relevant) |
| Italian co-funding (PON, PNRR) | School digitalisation, where relevant |

## Consortium profile

- **Liceo Vittoria Colonna, Rome** — public school, potential project partner
- **SARA Systems GmbH, Germany** — private company, AI/coding training packages for teachers and students

## Recipients

| Name | Address |
|---|---|
| Michele Minno | michele.minno@sara-systems.com |
| Luca Sbano | luca.sbano@sara-systems.eu |
| Markus Kirkilionis | markus.kirkilionis@sara-systems.eu |

## Schedule

Daily (weekdays). Configured as a Claude Code cloud routine with cron trigger.

## Files

| File | Description |
|---|---|
| `prompt.md` | Main prompt passed to Claude at each execution |
| `send_email.py` | SMTP email sender script (uses environment secrets) |
| `README.md` | This file |

## Environment secrets required

The following secrets must be configured in the Claude Code cloud routine environment:

| Variable | Description |
|---|---|
| `SMTP_HOST` | IONOS SMTP host (e.g. `smtp.ionos.eu`) |
| `SMTP_PORT` | SMTP port (`465` for SSL) |
| `SMTP_USER` | Sender address (`michele.minno@sara-systems.com`) |
| `SMTP_PASSWORD` | IONOS account password |

> **Note:** Never commit these values to the repository. Always set them as environment secrets in the Claude Code routine settings.

## Setup

1. Clone this repo and associate it with a Claude Code cloud routine
2. Add the four environment secrets listed above in the routine settings
3. Set the cron schedule (daily, weekdays recommended)
4. Run once manually to verify the email is delivered correctly

## Related

- [Erasmus+ opportunities](https://erasmus-plus.ec.europa.eu/opportunities/opportunities-for-organisations)
- [EU Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals)
- [Digital Europe Programme](https://digital-strategy.ec.europa.eu/en/activities/digital-programme)
