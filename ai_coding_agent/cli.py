import argparse
from ai_coding_agent.orchestrator import ProjectOrchestrator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ai-coding-agent",
        description="AI Coding 项目自动开发 Agent"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_parser = subparsers.add_parser("plan", help="只生成需求、架构和任务")
    plan_parser.add_argument("--idea", required=True, help="项目想法")
    plan_parser.add_argument("--name", required=True, help="项目名称")
    plan_parser.add_argument("--provider", default="mock", choices=["mock", "openai"])

    run_parser = subparsers.add_parser("run", help="运行完整开发流程")
    run_parser.add_argument("--idea", required=True, help="项目想法")
    run_parser.add_argument("--name", required=True, help="项目名称")
    run_parser.add_argument("--provider", default="mock", choices=["mock", "openai"])

    test_parser = subparsers.add_parser("test", help="测试已有项目")
    test_parser.add_argument("--name", required=True, help="项目名称")

    report_parser = subparsers.add_parser("report", help="查看报告路径")
    report_parser.add_argument("--name", required=True, help="项目名称")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    orchestrator = ProjectOrchestrator()

    if args.command == "plan":
        spec = orchestrator.plan(args.name, args.idea, args.provider)
        print(f"计划已生成：{spec.project_dir}")

    elif args.command == "run":
        spec = orchestrator.run(args.name, args.idea, args.provider)
        print(f"完整流程已运行：{spec.project_dir}")
        print(f"最终报告：{spec.project_dir / 'final_report.md'}")

    elif args.command == "test":
        print(orchestrator.test(args.name))

    elif args.command == "report":
        print(orchestrator.report_path(args.name))


if __name__ == "__main__":
    main()
