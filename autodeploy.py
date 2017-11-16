#!/usr/bin/env python

import sys

from src.cli import CONF
from src.otc_manager import OTC
from src.deploy_vpc import undeploy_vpc
from src.deploy_win_app_exchange import deploy_winapp_exchange
from src.deploy_chef_base import deploy as deploy_chef_base
from src.deploy_chef_apache import deploy as deploy_chef_apache
from src.show import Show
from src.excepts import DeployException


def main():
    CONF(sys.argv[1:])
    OTC.create_connection()

    if CONF.show:
        Show.show()

    deploy = {
        'winapp-exchange': deploy_winapp_exchange,
        'chef-base': deploy_chef_base,
        'chef-apache': deploy_chef_apache
    }

    undeploy = {
        'vpc': undeploy_vpc
    }

    try:
        if CONF.deploy:
            df = deploy.get(CONF.deploy)
            if df:
                df()

        if CONF.undeploy:
            udf = undeploy.get(CONF.undeploy)
            if udf:
                udf()
    except DeployException as e:
        print e.message


if __name__ == "__main__":
    main()

