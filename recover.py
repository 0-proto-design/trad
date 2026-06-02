import json

log_path = "/Users/kento/.gemini/antigravity/brain/1e6b6251-34b5-4449-a765-cf8dffc3521d/.system_generated/logs/transcript.jsonl"
file_path = "/Users/kento/Desktop/git hub/trad/recruit.html"

with open(file_path, "r") as f:
    content = f.read()

with open(log_path, "r") as f:
    for line in f:
        try:
            data = json.loads(line)
        except:
            continue
            
        if data.get("type") == "PLANNER_RESPONSE" and "tool_calls" in data:
            for call in data["tool_calls"]:
                if call["name"] == "replace_file_content" or call["name"] == "multi_replace_file_content":
                    args = call["args"]
                    target_file = args.get("TargetFile", "")
                    if target_file.strip('"') == file_path:
                        # Wait, we need to know if this tool call was actually executed successfully.
                        # It's better to find the CODE_ACTION that represents the result?
                        # Actually, just parse the CODE_ACTION
                        pass
