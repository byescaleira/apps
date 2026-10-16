#!/usr/bin/env python3
import argparse
import datetime
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE = os.path.join(ROOT, "source.json")


def main():
    parser = argparse.ArgumentParser(description="Adds a release to an app in source.json.")
    parser.add_argument("bundle_id")
    parser.add_argument("version")
    parser.add_argument("build")
    parser.add_argument("download_url")
    parser.add_argument("size", type=int)
    parser.add_argument("--min-os", default="27.0")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    with open(SOURCE) as handle:
        source = json.load(handle)
    app = next((a for a in source["apps"] if a["bundleIdentifier"] == args.bundle_id), None)
    if app is None:
        raise SystemExit(f"{args.bundle_id} is not in source.json")

    release = {
        "version": args.version,
        "buildVersion": args.build,
        "date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "localizedDescription": args.notes,
        "downloadURL": args.download_url,
        "size": args.size,
        "minOSVersion": args.min_os,
    }
    app["versions"] = [v for v in app["versions"]
                       if (v["version"], v.get("buildVersion")) != (args.version, args.build)]
    app["versions"].insert(0, release)
    app["version"] = release["version"]
    app["versionDate"] = release["date"]
    app["versionDescription"] = release["localizedDescription"]
    app["downloadURL"] = release["downloadURL"]
    app["size"] = release["size"]

    with open(SOURCE, "w") as handle:
        json.dump(source, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
    print(f"{app['name']} {args.version} ({args.build}) added")


if __name__ == "__main__":
    main()
