import unittest

from quick_eks_cross_az.lib import CrossAzLogger

# manually run for now


class TestInc(unittest.TestCase):
    # def test_setup(self):
    #     cal = CrossAzLogger()
    #     cal.setup_clients()

    # def test_cred(self):
    #     cal = CrossAzLogger()
    #     cal.setup_clients()
    #     self.assertTrue(cal.test_credentials())

    # def test_deploy(self):
    #     cal = CrossAzLogger(verbose=True)
    #     cal.setup_clients()
    #     cf = cal.get_cloudformation()
    #     cluster_name =cal.get_cluster_name_from_kube_context()
    #     vpc_id = cal.get_eks_cluster_vpc_id(cluster_name)
    #     cal.deploy_cf_stack(cf, "asaf-temp-test",{"eksVpcId":vpc_id})

    # def test_delete(self):
    #     cal = CrossAzLogger(verbose=True)
    #     cal.setup_clients()
    #     cf = cal.get_cloudformation()
    #     cluster_name =cal.get_cluster_name_from_kube_context()
    #     vpc_id = cal.get_eks_cluster_vpc_id(cluster_name)
    #     cal.deploy_cf_stack(cf, "asaf-temp-test",{"eksVpcId":vpc_id})
    #     cal.cleanup_and_delete_cf_stack("asaf-temp-test")

    # def test_pod_upload(self):
    #     cal = CrossAzLogger(verbose=True)
    #     cal.setup_clients()
    #     cf = cal.get_cloudformation()
    #     cluster_name =cal.get_cluster_name_from_kube_context()
    #     vpc_id = cal.get_eks_cluster_vpc_id(cluster_name)
    #     cal.deploy_cf_stack(cf, "asaf-temp-test",{"eksVpcId":vpc_id})
    #     cal.upload_pod_ips("asaf-temp-test")
    #     cal.cleanup_and_delete_cf_stack("asaf-temp-test")

    # def test_run(self):
    #     cal = CrossAzLogger(verbose=True)
    #     cal.setup_clients()
    #     cal.run()

    def test_summary(self):
        cal = CrossAzLogger(verbose=True)
        cal.print_summary("cross-az.csv")

    # def test_athena(self):
    #     cal = CrossAzLogger(verbose=True)
    #     cal.setup_clients()
    #     query_id = cal.get_named_queries_ids_in_stack(cal.cf_stack_name)[0]
    #     cal.run_athena_named_query_to_csv(query_id, 'mm-asaf-test-temp-bucket', 'aaa')
