# claude-routine-european-grants

Daily monitor for EU funding opportunities (Erasmus+, Horizon Europe, Digital Europe) — Claude Code cloud routine.

## What it does

This Claude Code cloud routine runs daily and:

1. Searches for new or updated EU funding calls published in the last 24–48 hours, relevant to a **public-private consortium** (school + private company) working on AI, coding, digital skills, and teacher/student training
2. Flags calls with deadlines approaching within 30 days
3. Sends a bilingual summary email (English + Italian) to the consortium team

## Monitored programmes

| Programme                          | Focus                                                          |
| ---------------------------------- | -------------------------------------------------------------- |
| Erasmus+                           | Cooperation Partnerships, Teacher Academies, Digital Education |
| Horizon Europe                     | Digital, Industry & Space cluster; Civil Society pillar        |
| Digital Europe Programme (DIGITAL) | Advanced digital skills                                        |
| Creative Europe                    | Educational/media content (when relevant)                      |
| Italian co-funding (PON, PNRR)     | School digitalisation, where relevant                          |

## Consortium profile

- **Liceo Vittoria Colonna, Rome** — public school, potential project partner
- **SARA Systems GmbH, Germany** — private company, AI/coding training packages for teachers and students

## Recipients

| Name               | Address                            |
| ------------------ | ---------------------------------- |
| Michele Minno      | michele.minno@sara-system.com      |
| Luca Sbano         | luca.sbano@sara-systems.eu         |
| Markus Kirkilionis | markus.kirkilionis@sara-systems.eu |

## Schedule

Daily (weekdays). Configured as a Claude Code cloud routine with cron trigger.

## Files

| File            | Description                                         |
| --------------- | --------------------------------------------------- |
| `prompt.md`     | Main prompt passed to Claude at each execution      |
| `send_email.py` | SMTP email sender script (uses environment secrets) |
| `README.md`     | This file                                           |

## Environment secrets required

Email is sent via the **Mailgun HTTP API** (not SMTP) because the routine's
sandboxed execution environment only permits outbound HTTPS traffic — raw
SMTP connections (e.g. to IONOS on port 465) are blocked by the network
policy and time out.

| Variable               | Required | Description                                                                                         |
| ---------------------- | -------- | --------------------------------------------------------------------------------------------------- |
| `MAILGUN_API_KEY`      | yes      | Mailgun private API key                                                                             |
| `MAILGUN_DOMAIN`       | yes      | Mailgun sending domain (e.g. `mg.sara-system.com`, or the sandbox domain on the free plan)          |
| `MAILGUN_API_BASE_URL` | no       | Defaults to `https://api.mailgun.net/v3`; use `https://api.eu.mailgun.net/v3` for EU-region domains |
| `MAILGUN_FROM`         | no       | Defaults to `European Grants Monitor <mailgun@MAILGUN_DOMAIN>`                                      |

> **Note:** Never commit these values to the repository. Always set them as environment secrets in the Claude Code routine settings.
>
> On Mailgun's free sandbox domain, only "Authorized Recipients" added in the
> Mailgun dashboard can receive mail — add all three recipients below there,
> or verify a custom domain to send without restriction.

## Setup

1. Clone this repo and associate it with a Claude Code cloud routine
2. Add the Mailgun environment secrets listed above in the routine settings
3. Set the cron schedule (daily, weekdays recommended)
4. Run once manually to verify the email is delivered correctly

## Related

- [Erasmus+ opportunities](https://erasmus-plus.ec.europa.eu/opportunities/opportunities-for-organisations)
- [EU Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/calls-for-proposals)
- [Digital Europe Programme](https://digital-strategy.ec.europa.eu/en/activities/digital-programme)
