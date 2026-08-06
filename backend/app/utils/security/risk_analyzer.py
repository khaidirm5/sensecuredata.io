from pathlib import Path


class RiskAnalyzer:
    MAX_SAFE_SIZE = 10 * 1024 * 1024  # 10 MB

    @classmethod
    def analyze(
        cls,
        file_path: str | Path,
        *,
        is_duplicate: bool,
    ) -> dict:
        file = Path(file_path)

        threats: list[str] = []
        score = 100

        if is_duplicate:
            threats.append("DUPLICATE")
            score -= 20

        if file.stat().st_size > cls.MAX_SAFE_SIZE:
            threats.append("LARGE_FILE")
            score -= 10

        score = max(score, 0)

        if score >= 90:
            risk = "SAFE"
        elif score >= 70:
            risk = "LOW"
        elif score >= 50:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        return {
            "risk_level": risk,
            "security_score": score,
            "threat_type": ",".join(threats) if threats else "NONE",
            "scan_details": {
                "message": (
                    "No threats detected." if not threats else "Threats detected."
                ),
                "threats": threats,
            },
        }
